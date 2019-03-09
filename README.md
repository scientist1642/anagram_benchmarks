This is the unnoficial repo for calculating running times of helmes challenge solutions. Benchmark tries to not allow app use a cached version of file, as it was explicitely stated that file should be referenced from disk. Right now it does so by keeping copies of the same dictionary files. 
Obviously timing will be differt on different machines, so you can run this on yours (be careful with untrusted solutions).

Open an issue if you want to add your solution in results.

# Usage
`git clone https://github.com/scientist1642/anagram_benchmarks --recursive`

`python3 benchmark.py [repo_name | all]` 
`python3 benchmark.py all` - benchmark all solutions - takes a long time
`python3 benchmark.py username/reponame` - benchmark a specific solution.

To generate markdown table:

`cat benchmark_results.csv | python3 tools/mdtable.py -separator:, `

### Adding a new solution 
Update `repos.txt` and 
`git submodule add https://github.com/adamsont/helmes_challenge.git solutions/adamsont/helmes_challenge`

## TODO 
Drop cache before each run with `echo 3 > /proc/sys/vm/drop_caches`a

## Results
Done on ubuntu 18.04 64bit virtualbox vm 2 cpu / Macos 2014 2ghz

| repo                        | lang | mean  | stdev |
|-----------------------------|------|-------|-------|
| intgr/anaXgram              | Rust | 8915  | 2431  |
| scientist1642/hlm_challenge | Cpp  | 6209  | 1160  |
| adamsont/helmes_challenge   | C    | 13390 | 2309  |
| gdantimi/helmeschallenge    | Java | 70105 | 9939  |



ubuntu 18.04 ryzen 1700x 8 core

| repo                        | lang | mean  | stdev |
|-----------------------------|------|-------|-------|
| intgr/anaXgram              | Rust | 7129  | 3141  |
| scientist1642/hlm_challenge | Cpp  | 4750  | 188   |
| adamsont/helmes_challenge   | C    | 10529 | 2110  |
