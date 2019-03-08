This is the unnoficial repo for calculating running times of helmes challenge solutions. Benchmark tries to not allow app use a cached version of file, as it was explicitely stated that file should be referenced from disk. Right now it does so by keeping copies of the same dictionary files. 
Obviously timing will be differt on different machines, so you can run this on yours (be careful with untrusted solutions).

open an issue if you want to add your solution in results.

# Usage
add your solution in `repos.txt`.

`python3 benchmark.py [repo_name | all]` 

`python3 benchmark.py all` - benchmark all solutions - takes a long time

`python3 benchmark.py username/reponame` - benchmark a specific solution.

To generate markdown table:

`cat benchmark_results.csv | python3 tools/mdtable.py -separator:, `


## TODO 
drop cache before each run with `echo 3 > /proc/sys/vm/drop_caches`a

## Results

| repo                        | lang | mean | stdev |
|-----------------------------|------|------|-------|
| scientist1642/hlm_challenge | Cpp  | 6683 | 874   |
| intgr/anaXgram              | Rust | 8980 | 1188  |

