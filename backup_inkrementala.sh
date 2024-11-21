#!/bin/bash
SEGURTASUNA_DIR="/Segurtasuna"
BACKUP_BASE="/var/tmp/Backups"

GAUR=$(date +%Y-%m-%d)
BIHAR=$(date -d "tomorrow" +%Y-%m-%d)
ETZI=$(date -d "2 days" +%Y-%m-%d)

HELBURUA=""
if [ -d "$BACKUP_BASE/$GAUR" ]; then
    HELBURUA="$BACKUP_BASE/$GAUR"
elif [ -d "$BACKUP_BASE/$BIHAR" ]; then
    HELBURUA="$BACKUP_BASE/$BIHAR"
elif [ -d "$BACKUP_BASE/$ETZI" ]; then
    HELBURUA="$BACKUP_BASE/$ETZI"
else
    echo "Ez da karpeta baliogarririk aurkitu."
    exit 1
fi

rsync -av --link-dest="$HELBURUA" "$SEGURTASUNA_DIR/" "$HELBURUA/"

echo "Kopia eginda: $HELBURUA"
