$StopWatch = [system.diagnostics.stopwatch]::StartNew()
$n = 250
for ($i=0; $i -le $n; $i++) {
    # Write-Host $i
    ./main.py
}
$StopWatch.Stop()
Write-Host "Execution time: $($StopWatch.Elapsed.TotalMilliseconds) milliseconds"
