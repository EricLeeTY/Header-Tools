import os
import time
# import header_tool
# header_tool = header_tool.Header_Tool(__file__)
# header_tool.get_modified_time()
import arrow
modTimesinceEpoc = os.path.getmtime(__file__)
# Convert seconds since epoch to readable timestamp
modificationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modTimesinceEpoc))
print("Last Modified Time : ", modificationTime)
timestamp = arrow.get(modificationTime)
print(timestamp)