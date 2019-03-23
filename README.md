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

| repo                        | lang | mean  | stdev | cpu_info                                         |
|-----------------------------|------|-------|-------|--------------------------------------------------|
| intgr/anaXgram              | Rust | 9025  | 1574  | Intel(R) Core(TM) i7-4750HQ CPU @ 2.00GHz 2 PROC |
| scientist1642/hlm_challenge | Cpp  | 6137  | 1259  | Intel(R) Core(TM) i7-4750HQ CPU @ 2.00GHz 2 PROC |
| adamsont/helmes_challenge   | C    | 13431 | 3415  | Intel(R) Core(TM) i7-4750HQ CPU @ 2.00GHz 2 PROC |
| gdantimi/helmeschallenge    | Java | 73790 | 13149 | Intel(R) Core(TM) i7-4750HQ CPU @ 2.00GHz 2 PROC |
| Lauri-Nomme/filteranagrams  | C    | 8374  | 1358  | Intel(R) Core(TM) i7-4750HQ CPU @ 2.00GHz 2 PROC |
| f0c14e08c2/adfa074714       | Java | 6516  | 1046  | Intel(R) Core(TM) i7-4750HQ CPU @ 2.00GHz 2 PROC |

ubuntu 18.04 ryzen 1700x 8 core

| repo                        | lang | mean  | stdev | cpu_info                                      |
|-----------------------------|------|-------|-------|-----------------------------------------------|
| intgr/anaXgram              | Rust | 7130  | 3044  | AMD Ryzen 7 1700 Eight-Core Processor 16 PROC |
| scientist1642/hlm_challenge | Cpp  | 4762  | 197   | AMD Ryzen 7 1700 Eight-Core Processor 16 PROC |
| adamsont/helmes_challenge   | C    | 11397 | 3000  | AMD Ryzen 7 1700 Eight-Core Processor 16 PROC |
| gdantimi/helmeschallenge    | Java | 55480 | 11278 | AMD Ryzen 7 1700 Eight-Core Processor 16 PROC |
| Lauri-Nomme/filteranagrams  | C    | 3833  | 171   | AMD Ryzen 7 1700 Eight-Core Processor 16 PROC |

i7-7700HQ

| repo                             | lang | mean  | stdev | cpu_info                                         |
|----------------------------------|------|-------|-------|--------------------------------------------------|
| adamsont/helmes_challenge        | C    | 15745 | 1144  | Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz 8 PROC |
| intgr/anaXgram                   | Rust | 12743 | 1544  | Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz 8 PROC |
| scientist1642/hlm_challenge      | Cpp  | 9575  | 1621  | Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz 8 PROC |
| Lauri-Nomme/filteranagrams       | C    | 11959 | 1312  | Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz 8 PROC |
| gdantimi/helmeschallenge         | Java | 55880 | 8518  | Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz 8 PROC |
| Lauri-Nomme/filteranagrams-pread | C    | 11637 | 1250  | Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz 8 PROC |

i7-6700HQ

| repo                        | lang | mean | stdev | cpu_info                                         |
|-----------------------------|------|------|-------|--------------------------------------------------|
| intgr/anaXgram              | Rust | 1901 | 211   | Intel(R) Core(TM) i7-6700HQ CPU @ 2.60GHz 8 PROC |
| scientist1642/hlm_challenge | Cpp  | 2837 | 1488  | Intel(R) Core(TM) i7-6700HQ CPU @ 2.60GHz 8 PROC |
| gdantimi/helmeschallenge    |      |      |       |                                                  |
| adamsont/helmes_challenge   | C    | 5118 | 899   | Intel(R) Core(TM) i7-6700HQ CPU @ 2.60GHz 8 PROC |
| Lauri-Nomme/filteranagrams  | C    | 2996 | 329   | Intel(R) Core(TM) i7-6700HQ CPU @ 2.60GHz 8 PROC |
