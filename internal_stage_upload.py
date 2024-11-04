# Upload files to internal stage while optimizing warehouse use and keeping partitioning.

### TODO
#X login
#2. get whs size
    #X set whs
#3. start async loop
## bonus
# - progress bar
# - output log

from snowflake.snowpark import Session
from snowflake.core import Root, warehouse

# GLOBALS
CONNECTION = ''
WAREHOUSE = ''
SOUCE = ''

# Login
session = Session.builder.config("connection_name", CONNECTION).create()

# Make root
root = Root(session)

# Set warehouse
session.use_warehouse(WAREHOUSE)

# Get Warehouse size 
size = root.warehouses[session.get_current_warehouse()].fetch().warehouse_size
