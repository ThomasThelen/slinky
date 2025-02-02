# Virtuoso

Slinky's graph database

## Enabling SPARQL Update

This folder contains a Dockerfile that runs the enable_update.sh script during startup. This creates a rule that allows the default user to perform SPARQL Updates.

## Protecting the Virtuoso SPARQL Endpoint

In order to protect Virtuoso's `sparql/` endpoint, follow [this](http://vos.openlinksw.com/owiki/wiki/VOS/VirtSPARQLProtectSQLDigestAuthentication) guide from Open Link. While performing 'Step 6', use the `Browse` button to locate the authentication function rather than copy+pasting `DB.DBA.HP_AUTH_SQL_USER;`, which is suggested by the guide. _This should be done for all new production deployments_.
