#!/bin/bash

browser_locales="engine/browser/locales"

copy_browser_locales() {
  langId="$1"
  
  if [ -z "$langId" ]; then
    echo "Error: No language ID provided."
    return 1
  fi
  
  mkdir -p "$browser_locales/$langId"
  
  if [ "$langId" = "en-US" ]; then
    # Remove any existing files starting with "zen" for en-US
    find "$browser_locales/$langId" -type f -name "zen*" -delete
    # Copy the en-US localization files
    rsync -av --exclude=.git "./l10n/en-US/browser/" "$browser_locales/$langId/"
  else
    # Remove any existing localization for the specified language
    rm -rf "$browser_locales/$langId/"
    # Copy the localization files for the specified language
    # Make sure the source directory exists
    if [ -d "./l10n/$langId/" ]; then
      rsync -av --exclude=.git "./l10n/$langId/" "$browser_locales/$langId/"
    else
      echo "Warning: Localization directory for $langId does not exist. Skipping."
    fi
  fi
}

LANG="$1"
echo "Copying language pack for $LANG"
copy_browser_locales "$LANG"
