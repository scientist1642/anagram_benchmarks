# Note
This is the unnoficial repo for calculating running times of helmes challenge solutions. Benchmark tries to not allow app use a cached version of file, as it was explicitely stated that file should be referenced from disk. Right now it does so by keeping copies of the same dictionary files. 
Obviously an architecture will have a big impact on timings, so you can run this on your machine if you can (be careful with untrusted solutions)

#Usage
solution list is in `repos.txt`

Run:
`python3 benchmark.py [repo_name | all]` 
`python3 benchmark.py all` -  to benchmark all solutions - takes a long time
`python3 benchmark.py username/reponame` - to benchmark a specific solution.

To generate markdown table:
`cat benchmark_results.csv | python3 tools/mdtable.py`

#TODO 
drop cache before each run with `echo 3 > /proc/sys/vm/drop_caches`


## Results

| repo                        | lang | mean | stdev |
|-----------------------------|------|------|-------|
| scientist1642/hlm_challenge | Cpp  | 6153 | 453   |
