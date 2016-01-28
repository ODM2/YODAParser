YODA-Tools
====
Prototyping a tool to validate and manage loading of YODA files

Command line:
```
yoda [command] [options]
```

Testing for validating a yoda file:
```
usage: yoda.py validate [-h] [--type TYPE] [--level LEVEL] [-c] yoda_file

positional arguments:
  yoda_file      yoda file name

optional arguments:
  -h, --help     show this help message and exit
  --type TYPE    data type: measurement, timeseries
  --level LEVEL  validation level: 1 for coarse, 2 for medium, 3 for fine
  -c, --cvtype   validate CV types
Example:
  $ python yoda.py validate --type timeseries --level 1 ./examples/YODA_TimeSeries_Example1_Template_0.3.1-alpha.yaml 
```
Testing for generating yodata file from xl file
```
usage: yoda.py generate [-h] [--type TYPE] xl_file out_file

positional arguments:
  xl_file      xl file name (input)
  out_file     yaml file name (output)

optional arguments:
  -h, --help   show this help message and exit
  --type TYPE  data type: measurement, timeseries
Example:
  $ python yoda.py generate --type measurement ./examples/YODA_Specimen_TEMPLATE_WORKING.xlsm generated_measurement.yaml
```

Intitial thoguhts:
  * yoda validate [format] [file] [strict?]
     * validates a yoda file. formats [TS-timeseries, SP-Specimens]
     * [strict] true(default). follow vocabs. false = allow loose
  * yoda loaddatabase [connection] [options] [strict?]
     * loads data to a specified database connection
     * [strict] true(default). follow vocabs. false = ADD terms
  * yoda load [yodafile] [url] [--validate=true]
     * load yoda file to a specified ODM2 Webservice
     * option to turn off validate
  * yoda get [datasetid] [url] [--format]
     *  get dataset from a ODM2 webservice in a specified format
  * yoda generate [input xlsx file] [output file]
     * generate and validate a yoda from specified XLSX file, save to file
  * yoda
     * opens a gui
  * yoda help
  * yoda cvsubmit [format] [file]
    * submit unknown controlled terms to cv service

### Credits

This work was supported by National Science Foundation Grants [EAR-1224638](http://www.nsf.gov/awardsearch/showAward?AWD_ID=1224638) and [ACI-1339834](http://www.nsf.gov/awardsearch/showAward?AWD_ID=1339834). Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation.
