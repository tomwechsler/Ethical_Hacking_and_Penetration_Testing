#Define a list to hold the system info objects
$systemInfo = @()

#Collect CPU information
$cpuInfo = Get-WmiObject -Class Win32_Processor
if ($cpuInfo) {
    $systemInfo += New-Object PSObject -Property @{
        "Component" = "CPU"
        "Name" = $cpuInfo.Name.Trim()
        "Cores" = $cpuInfo.NumberOfCores
        "Speed (GHz)" = [math]::Round($cpuInfo.MaxClockSpeed / 1000, 2)
    }
}

#Collect Memory information
$memInfo = Get-WmiObject -Class Win32_PhysicalMemory
if ($memInfo) {
    $totalMem = ($memInfo | Measure-Object -Property Capacity -Sum).Sum / 1GB
    if ($totalMem -gt 0) {
        $systemInfo += New-Object PSObject -Property @{
            "Component" = "Memory"
            "Name" = "Total Memory"
            "Cores" = ""
            "Speed (GHz)" = ""
            "Total Memory (GB)" = [math]::Round($totalMem, 2)
        }
    }
}

#Collect Disk information
$diskInfo = Get-WmiObject -Class Win32_LogicalDisk -Filter "DriveType = 3"
if ($diskInfo) {
    foreach ($disk in $diskInfo) {
        $systemInfo += New-Object PSObject -Property @{
            "Component" = "Disk"
            "Name" = $disk.DeviceID
            "Cores" = ""
            "Speed (GHz)" = ""
            "Total Memory (GB)" = ""
            "Size (GB)" = if ($disk.Size -and $disk.Size -ne 0) { [math]::Round($disk.Size / 1GB, 2) } else { "N/A" }
            "Free Space (GB)" = if ($disk.FreeSpace -and $disk.FreeSpace -ne 0) { [math]::Round($disk.FreeSpace / 1GB, 2) } else { "N/A" }
        }
    }
}

#Reorder and normalize properties for CSV export
$exportData = $systemInfo | Select-Object -Property @{
    Name = "Component"; Expression = { $_.Component }
}, @{
    Name = "Name"; Expression = { $_.Name }
}, @{
    Name = "Cores"; Expression = { $_.Cores }
}, @{
    Name = "Speed (GHz)"; Expression = { $_.Speed }
}, @{
    Name = "Total Memory (GB)"; Expression = { $_."Total Memory (GB)" }
}, @{
    Name = "Size (GB)"; Expression = { $_."Size (GB)" }
}, @{
    Name = "Free Space (GB)"; Expression = { $_."Free Space (GB)" }
}

#Export system information to CSV
$exportData | Export-Csv -Path "SystemInfoReport.csv" -NoTypeInformation -Force
Write-Host "System information report generated: SystemInfoReport.csv"