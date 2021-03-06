# Toy file pointer
rearrangement_file <- file.path("..", "data-tests", "toy_data.tsv")
#rearrangement_file <- file.path("tests", "data-tests", "toy_data.tsv")

# Toy file pointer
bad_rearrangement_file <- file.path("..", "data-tests", "bad_data.tsv")
#bad_rearrangement_file <- file.path("tests", "data-tests", "bad_data.tsv")

# Expected warnings for bad_rearrangement_file
expected_w <- c(
    "Warning: File is missing AIRR mandatory field(s): sequence",            
    "Warning: sequence_id(s) are not unique: IVKNQEJ01AJ44V, IVKNQEJ01AJ44V",
    "Warning: sequence_id is empty for row(s): 7",
    "Warning: rev_comp is not logical for row(s): 4",
    "Warning: productive is not logical for row(s): 1"
)

#### Rearrangement I/O  ####

context("Rearrangement I/O - good data")

test_that("read_airr loads a data.frame", {
    tbl_0 <- read_airr(rearrangement_file, "0")
    expect_true(is.data.frame(tbl_0))
})

test_that("read_arirr applies base", {
    tbl_0 <- read_airr(rearrangement_file, "0")
    tbl_1 <- read_airr(rearrangement_file, "1")
    expect_true(is.data.frame(tbl_1))
    expect_true(validate_airr(tbl_0))
    start_positions <- grep("_start$", names(tbl_0), perl=TRUE)
    expect_equivalent(tbl_0[, start_positions] - 1, tbl_1[, start_positions])
})


test_that("write_airr writes a file with logicals encoded T/F", {
    tbl <- read_airr(rearrangement_file)
    out_file <- file.path(tempdir(), "test_out.tsv")
    write_airr(tbl, out_file)
    expect_true(file.exists(out_file))
    reload_tbl <- read.delim(out_file, colClasses="character")
    expect_true(all(reload_tbl[['rev_comp']] == "T"))
    expect_equal(reload_tbl[['productive']],
                 c("T","T","F","T","T","F","F","F","T"))
})

context("Rearrangement I/O - bad data")

test_that("read_airr with bad data", {
    # Expect valid==FALSE
    bad_data <- suppressWarnings(read_airr(bad_rearrangement_file, "0"))
    expect_false(suppressWarnings(validate_airr(bad_data)))
    # Check error messages
    w <- capture_warnings(validate_airr(bad_data))
    expect_equal(w, expected_w)
})

test_that("write_airr writes a bad file, with warnings, with logicals T/T", {
    bad_data <- suppressWarnings(read_airr(bad_rearrangement_file, "0"))
    out_file <- file.path(tempdir(), "test_out.tsv")
    expect_warning(write_airr(bad_data, out_file))
    expect_true(file.exists(out_file))
    reload_tbl <- read.delim(out_file, colClasses="character")
    expect_equal(reload_tbl[['rev_comp']],
                c("T","T","T","","T","T","T","T","T","T","T"))
    expect_equal(reload_tbl[['productive']],
                 c("","T","F","T","T","F","F","F","T","T","T"))
})
