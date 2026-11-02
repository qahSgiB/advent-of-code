param (
    [string]$day="",
    [string]$folder=".",
    [string]$langs="py,hs",
    [string]$year = "2025",
    [string]$session="53616c7465645f5f3bead5ae267e20f5a07eeb858881e34371106a056918cf335d27461db88169cba4fb42f3da1067a98467c1ccec544f3949664c8949cd1f1b",
    [string]$templateDir="C:\Users\tomas\stuff\programming\aoc\util\"
)



function Aoc-Download-Input {
    param (
        [string]$inpFilePath
    )

    $webSession = New-Object Microsoft.PowerShell.Commands.WebRequestSession
    $cookie = New-Object System.Net.Cookie 

    $cookie.Name = "session"
    $cookie.Value = $session
    $cookie.Domain = ".adventofcode.com"

    $webSession.Cookies.Add($cookie)

    $inpFileUri = "https://adventofcode.com/$($year)/day/$($dayShort)/input"
    Invoke-WebRequest -Uri $inpFileUri -WebSession $webSession -OutFile $inpFilePath
}

function Aoc-Copy-Template {
    param (
        [string]$lang,
        [string]$destination
    )

    $templateLangDir = Join-Path $templateDir $lang
    $templateLangDir = Join-Path $templateLangDir "template"
    if (Test-Path $templateLangDir) {
        $templateFiles = Join-Path $templateLangDir "*"
        Copy-Item $templateFiles -Destination $destination -Recurse
    }
}

function Aoc-Create-Lang-Dir {
    param (
        [string]$dir,
        [string]$lang
    )
    
    $inpFilePath = Join-Path $dir "inp.txt"
    Aoc-Download-Input $inpFilePath

    Aoc-Copy-Template $lang $dir
}




$dayShort = $day
$dayLong = $day



if ($day -eq "") {
    $dayLong = Get-Date -Format "dd"
    if ($dayLong[0] -eq '0') {
        $dayShort = $dayLong[1]
    } else {
        $dayShort = $dayLong
    }
} elseif ($day.length -eq 1) {
    $dayLong = "0$($day)"
} elseif ($day.length -eq 2 -and $day[0] -eq "0") {
    $dayShort = $day[1]
}

$langss = $langs.Split(",")

New-Item -Path $folder -Name $dayLong -ItemType "directory" > $null
$dayDir = Join-Path $folder $dayLong

if ($langss.length -eq 1) {
    $lang = $langss[0]

    Aoc-Create-Lang-Dir $dayDir $lang
} elseif ($langss.length -gt 1) {
    foreach ($lang in $langss) {
        New-Item -Path $dayDir -Name $lang -ItemType "directory" > $null
        $langDir = Join-Path $dayDir $lang

        Aoc-Create-Lang-Dir $langDir $lang
    }
}