#!/bin/sh
# Pick a uuid for the app (or reuse existing one).
if ! [ -f installApp.uuid ]; then
    uuidgen > installApp.uuid
fi
UUID=$(cat installApp.uuid)
#create supporting folders
TOPDIR="$HOME/Library/Application Support/\
iPhone Simulator/6.0/Applications/$UUID/"
mkdir -p "$TOPDIR"
mkdir -p "$TOPDIR/Documents"
mkdir -p "$TOPDIR/Library"
mkdir -p "$TOPDIR/tmp"
mkdir -p "$TOPDIR/$1.app"

#copy all the app file to the simulators directory
cp -r * "$TOPDIR/$1.app"