#!/bin/bash

show_help() {
    cat << NANANA
usage:
    ./start.sh [options] [day [year]]

options:
    -h / --help
        displays this help
    -d / --dir
        destination directory
        (default: ".")
    -l / --langs
        comma separated list of languages, for which templates will be created
        (default: "py,hs")
    -s / --session
        aoc session id
        (default: 53616c7465645f5f5d95e9d63f5905bf7791c6dee75efbcc0d4754fdf54b890e6bcf6f9e4f443045007261be5c62e1dec8effb629c0e24b99569914b73d15190)
    -t / --template-dir
        directory where are templates stored
        (default: /home/tomas/stuff/programming/aoc/util/templates)
NANANA
}


aoc_download_input() {
    input_file="$1"

    cookie_header="Cookie: session=$session"
    url="https://adventofcode.com/$year/day/$day_short/input"
    wget --header="$cookie_header" -O "$input_file" "$url"
}

aoc_create_dir() {
    dir="$1"
    lang="$2"
    input_file="$3"

    lang_template_dir="$template_dir/$lang"
    if [ ! -d "$lang_template_dir" ]; then
        echo "template directory '$lang_template_dir' does not exists"
        return 1;
    fi

    cp -r "$lang_template_dir/." "$dir"
    cp "$input_file" "$dir/inp.txt"
}



##  getopt parsing

args=$(getopt -a -n start -o hd:l:s:t: --long help,dir:,langs:,session:,template-dir: -- "$@")
args_valid=$?
if [ $args_valid != 0 ]; then
    exit 1
fi

eval set -- $args # [todo]


##  params (defaults)

help=0
dir="."
langs_str="py,hs"
session="53616c7465645f5f5d95e9d63f5905bf7791c6dee75efbcc0d4754fdf54b890e6bcf6f9e4f443045007261be5c62e1dec8effb629c0e24b99569914b73d15190"
template_dir="/home/tomas/stuff/programming/aoc/util/templates"
day=$(date "+%d")
year="2022"


##  options parsing

while true; do
    case "$1" in
        -h | --help) help=1; shift ;;
        -d | --dir)
            shift
            dir="$1"
            shift
            ;;
        -l | --langs)
            shift
            langs_str="$1"
            shift
            ;;
        -s | --session)
            shift
            session="$1"
            shift
            ;;
        -t | --template_dir)
            shift
            template_dir="$1"
            shift
            ;;
        --) shift; break ;;
        *)
            echo "run: unrecognized option '$1'";
            exit 1
            ;;
    esac
done


##  positional arguments parsing

if [ $# -ge 1 ]; then
    day="$1"
    shift
fi

if [ $# -ge 1 ]; then
    year="$1"
    shift
fi


##  help

if [ $help = 1 ]; then
    show_help
    exit 0
fi


##  run

day_short="$day"
day_long="$day"
if [ ${#day} = 1 ]; then
    day_long="0${day}"
elif [ ${#day} = 2 -a "${day:0:1}" = "0" ]; then
    day_short="${day:1:1}"
fi


IFS="," read -a langs <<< "$langs_str"

if [ ! -d "$dir" ]; then
    echo "destination directory '$dir' does not exists"
    exit 1
fi

day_dir="$dir/$day_long"
if [ -d "$day_dir" ]; then
    echo "destination day directory '$day_dir' already exists"
    exit 1
fi
mkdir "$day_dir"

temp_input_file="$day_dir/temp_inp.txt"
aoc_download_input "$temp_input_file"

if [ ${#langs[@]} = 1 ]; then
    aoc_create_dir "$day_dir" "${langs[0]}" "$temp_input_file"
else
    for lang in "${langs[@]}"; do
        lang_dir="$day_dir/$lang"
        mkdir "$lang_dir"
        aoc_create_dir "$lang_dir" "$lang" "$temp_input_file"
    done
fi

rm "$temp_input_file"