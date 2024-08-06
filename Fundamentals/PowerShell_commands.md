## User administration

| Command    | Description                                                           |
|------------|-----------------------------------------------------------------------|
| New-LocalUser    | Creates a new local user account                                |
| Set-LocalUser    | Modifies a local user account                                   |
| Remove-LocalUser | Deletes a local user account                                    |
| New-LocalGroup   | Creates a new local security group                              |
| Remove-LocalGroup| Deletes a local security group                                  |
| Add-LocalGroupMember | Adds a user to a local security group                       |
| Get-LocalUser    | Gets information about local user accounts                      |
| Get-LocalGroup   | Gets information about local security groups                    |
| Set-LocalGroup   | Modifies a local security group                                 |

## Basic commands

| Command | Description                                      |
|---------|--------------------------------------------------|
| Get-Content | Gets the content of the item at the specified location |
| Set-Location | Sets the current working location to a specified location |
| Copy-Item    | Copies an item from one location to another |
| Get-Date     | Gets the current date and time |
| Write-Output | Sends the specified objects to the next command in the pipeline |
| Exit-PSSession | Ends an interactive session with a remote computer |
| New-Item     | Creates a new item |
| Move-Item    | Moves an item from one location to another |
| Get-Location | Gets information about the current working location |

## Network 

| Command    | Description                                                           |
|------------|-----------------------------------------------------------------------|
| Resolve-DnsName | Resolves a DNS name to an IP address |
| Get-NetIPAddress | Gets the IP address configuration |
| Get-NetAdapter | Gets the basic network adapter properties |
| Get-NetTCPConnection | Gets TCP connections |
| Test-Connection | Sends ICMP echo request packets ("pings") to one or more computers |
| Get-NetRoute   | Gets the IP route table |
| Test-NetConnection | Displays diagnostic information for a connection |

## File tools

| Command   | Description                                                           |
|-----------|-----------------------------------------------------------------------|
| Split-Path | Returns the specified part of a path |
| Get-Volume | Gets the specified volume object, or all volume objects if no volume is specified |
| Copy-Item  | Copies an item from one location to another |
| Compare-Object | Compares two sets of objects |
| Get-ChildItem | Gets the items and child items in one or more specified locations |
| Select-String | Finds text in strings and files |
| Get-Command | Gets all commands |
| Get-Partition | Gets the partition objects associated with the specified disk |
| Get-Process | Gets the processes that are running on the local computer |
| Get-FileHash | Computes the hash value for a file by using a specified hash algorithm |
| Mount-DiskImage | Mounts a disk image (virtual hard disk or ISO) |
| Rename-Item | Renames an item in a PowerShell provider namespace |
| Remove-Item  | Deletes the specified items |
| Sort-Object | Sorts objects by property values |
| Dismount-DiskImage | Dismounts a disk image (virtual hard disk or ISO) |
| Update-Help | Downloads and installs the newest help files for PowerShell modules |
| Measure-Object | Calculates the numeric properties of objects, and the characters, words, and lines in string objects |

## Process control

| Command  | Description                                                                 |
|----------|-----------------------------------------------------------------------------|
| Start-Process | Starts one or more processes on the local computer |
| Start-Job    | Starts a PowerShell background job |
| Get-Process  | Gets the processes that are running on the local computer |
| Get-ScheduledTask | Gets the scheduled tasks on the local computer |

## Rights

| Command | Description                                                      |
|---------|------------------------------------------------------------------|
| Set-ItemProperty | Changes the value of a property |
| Set-LocalGroup  | Modifies a local security group |
| Set-Acl         | Changes the security descriptor of a specified resource |
| Set-Owner       | Changes the owner of a specified resource |

## System monitoring

| Command  | Description                                                      |
|----------|------------------------------------------------------------------|
| Get-WinEvent | Gets events from event logs on the local and remote computers |
| Start-ScheduledTask | Starts a registered scheduled task |
| Get-ScheduledTask | Gets the scheduled tasks on the local computer |
| Get-PSDrive | Gets the drives in the current session |
| Get-ChildItem | Gets the items and child items in one or more specified locations |
| Stop-Process | Stops one or more running processes |
| Get-Item    | Gets the item at the specified location |
| Get-Process | Gets the processes that are running on the local computer |
| Get-Uptime  | Gets the uptime of the computer |

## Miscellaneous

| Command  | Description                                                                 |
|----------|-----------------------------------------------------------------------------|
| Set-Alias | Creates or changes an alias |
| Select-String | Finds text in strings and files |
| Set-Location | Sets the current working location to a specified location |
| Clear-Host | Clears the display in the host program |
| Write-EventLog | Writes an event to an event log |
| Get-WmiObject | Gets instances of WMI classes or information about the available classes |
| Get-PnpDevice | Returns information about PnP devices |
| Set-Content | Writes or replaces the content in an item with new content |
| Stop-Computer | Stops (shuts down) local and remote computers |
| Start-Sleep | Suspends the activity in a script or session for the specified period of time |
| Measure-Command | Measures the time it takes to run script blocks and cmdlets |
| Get-ComputerInfo | Gets a consolidated object of system and operating system properties |
| Write-Host | Writes customized output to a host |
| Watch-Command | Runs a command repeatedly, displaying its output and errors until stopped |
| Measure-Object | Calculates the numeric properties of objects, and the characters, words, and lines in string objects |
| Get-Help | Displays information about PowerShell commands and concepts |
| Get-Command | Gets all commands |