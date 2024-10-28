# Upload files to internal stage while optimizing warehouse use and keeping partitioning.

### TODO
#X login
#2. get whs size
    #- set whs
#3. start async loop
## bonus
# - progress bar
# - output log

from snowflake.snowpark import Session

# Login
session = Session.builder.config("connection_name", "my_connection").create()
