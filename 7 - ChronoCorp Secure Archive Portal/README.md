# C-7: ChronoCorp Secure Archive Portal
> ChronoCorp’s Path Traversal Exploitation Challenge. Try to access the hidden doc to get the flag. [View The Site Here](https://web.archive.org/web/20250714004026/http://ctf.nzcsc.org.nz:52700/)

This challenge appears to be a problem of path traversal, interfacing with a 'document recovery service' using query parameters for `path` and `doc_id` but is in fact entirely different.
Accessing the site's [robots.txt](https://web.archive.org/web/20250714004127/http://ctf.nzcsc.org.nz:52700/robots.txt) shows two disallowed folders, an allowed folder, and a sitemap. The only page that exists is [/server_assets](https://web.archive.org/web/20250714004258/http://ctf.nzcsc.org.nz:52700/server_assets/). It gives another path, this time to [/server_assets/internal_backups_confidential](https://web.archive.org/web/20250714004331/http://ctf.nzcsc.org.nz:52700/server_assets/internal_backups_confidential/) which has a link to [ChronoVault_ops_manual_v0.9.txt.bak](https://web.archive.org/web/20250714004403/http://ctf.nzcsc.org.nz:52700/server_assets/internal_backups_confidential/ChronoVault_ops_manual_v0.9.txt.bak).
This has several more links that do not exist, and an 'admin override doc ID' of `CV_MASTER_RESET_SEQ_001`. When this is entered as a query parameter ([/docs/retrieve?doc_id=CV_MASTER_RESET_SEQ_001](https://web.archive.org/web/20250714004500/http://ctf.nzcsc.org.nz:52700/docs/retrieve?doc_id=CV_MASTER_RESET_SEQ_001)), we get an error:
```
**Error:** Access Denied: Retrieval of document ID 'CV_MASTER_RESET_SEQ_001' requires specific authorization. Expected HTTP header 'X-Chrono-Auth: Override_Approved_Level9'.
```
Adding this request using the Network tab in the browser's developer tools gives us the flag:
![[7 - ChronoCorp Secure Archive Portal/flag.png]]
*Due to the special header required, we are unable to archive this page.*