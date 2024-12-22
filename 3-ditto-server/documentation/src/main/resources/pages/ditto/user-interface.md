---
title: Ditto Explorer User Interface
tags: [getting_started]
keywords: ui, sandbox, demo, trial
permalink: user-interface.html
topnav: topnav
---

## Introduction

There is a browser based user interface to explore things, policies and connections.
The UI can be used to access the REST API of any Ditto instance.
Several Ditto instances can be configured as "Environments"

{% include image.html file="pages/ui/screenshot_introduction.png" alt="UI example screenshot" caption="Ditto Explorer UI" max-width=800 url="https://eclipse-ditto.github.io/ditto/index.html?primaryEnvironmentName=ditto_sandbox" %}


## How to use

The latest version of the Explorer UI is available online [here](https://eclipse-ditto.github.io/ditto/index.html?primaryEnvironmentName=ditto_sandbox){:target="_blank"}

There is also a Docker image prepared to server the latest version by docker:
```bash
# to start the latest released UI version:
docker run -p 8088:8080 eclipse/ditto-ui

# or to start the latest nightly instead:
docker run -p 8088:8080 eclipse/ditto-ui:nightly
```

## Configuration options via environments

You can use the Explorer UI with different Ditto instances and switch easily between them.
For that, the Ditto-UI can be configured with so called `Environments`.

For example, you can work with your **local running Ditto instance** and the remote Eclipse Ditto **sandbox instance**.
Another example would be to use different stages of Ditto like **development**, **test** and **production**.

Those environments are either stored in the local storage of the user's browser
(and can also be completely edited there via the "Environments" tab of the UI),
or they (as a template, because the user's local storage has priority) can be loaded via a JSON file served via HTTP.

### Create a new environment
To create a new environment you just need to specify
* a unique name
* the api URI to reach Ditto
* whether it is a Ditto 2 or Ditto 3 version (only relevant if you want to use the connectivity API of Ditto prior to version 3)

{% include image.html file="pages/ui/screenshot_add_environment.png" alt="Screenshot how to add an environment" caption="Create a new environment" max-width=800 %}

### Selecting an environment
Select an environment in the drop down in the upper right:
{% include image.html file="pages/ui/screenshot_select_environment.png" alt="Screenshot how to select an environment" caption="Select a new environment" max-width=400 %}


### Control environments by URL parameters

The following Ditto UI query parameters can be used to control environments:

| URL query parameter      | Description                                        |
|--------------------------|----------------------------------------------------|
| `primaryEnvironmentName` | Name of an environment to be selected by default   |
| `environmentsURL`        | URL to a json file with environment configurations |

For example, you can provide your own environment template at a publicly available HTTP endpoint `https://<ditto-hostname>/ui-environments.json` and
pre-select choosing environment name `dev` (being part of the `ui-environments.json` file):
```
https://<ditto-hostname>/ui/?environmentsURL=/ui-environments.json&primaryEnvironmentName=dev
```

### Available environment configuration

A single "Environment" is defined as (Typescript type - from which the resulting JSON can be simply inferred):
```ts
type Environment = {
    /** The Ditto API URI to use, without the `/api/2` part */
    api_uri: string,
    /** The Ditto main version, either `2` or `3` */
    ditto_version: number,
    /** Whether to hide the "Policies" tab */
    disablePolicies?: boolean,
    /** Whether to hide the "Connections" tab */
    disableConnections?: boolean,
    /** Whether to hide the "Operations" tab */
    disableOperations?: boolean,
    /** The authorization settings for the UI */
    authSettings?: AuthSettings,
    /** A comma separated list of namespaces to perform Thing searches in */
    searchNamespaces?: string,
    /** Holds templates for well known (feature) messages */
    messageTemplates?: any,
    /** Contains a list of fields to be shown as additional columns in the Things search result table */
    fieldList?: FieldListItem[],
    /** Contains well known filters which should be suggested when typing in the Things search field */
    filterList?: string[],
    /** Holds a list of "pinned" things */
    pinnedThings?: string[],
    /** Holds a list of recently opened Policies in the "Policy" tab */
    recentPolicyIds?: string[],
}

type AuthSettings = {
    /** Contains the settings for the 'main' user authentication, accessing things+policies */
    main: MainAuthSettings,
    /** Contains the settings for the 'devops' user authentication, accessing connections+operations */
    devops: CommonAuthSettings,
    /** The shared OpenID Connect (OIDC) provider configuration with the provider as key and the configuration as value */
    oidc: Record<string, OidcProviderConfiguration>
}

type CommonAuthSettings = {
    /** The authentication method to apply */
    method: AuthMethod,
    /** Authentication settings for SSO (OIDC) based authentication */
    oidc: OidcAuthSettings,
    /** Authentication settings for Bearer authentication (manually providing a Bearer token to the UI) */
    bearer: BearerAuthSettings
    /** Authentication settings for Basic authentication */
    basic: BasicAuthSettings,
}

type MainAuthSettings = CommonAuthSettings & {
    /** Authentication settings for Pre-Authenticated authentication */
    pre: PreAuthSettings
}

type OidcProviderConfiguration = UserManagerSettings /* from 'oidc-client-ts' */ & {
    /** The name used in the drop-down list of available OIDC providers */
    displayName: string,
    /** Configures the field to use as 'Bearer' token from the response of the OIDC provider's /token endpoint, e.g. either "access_token" or "id_token" */
    extractBearerTokenFrom: string
}

export enum AuthMethod {
    oidc='oidc',
    basic='basic',
    bearer='bearer',
    pre='pre'
}

export type OidcAuthSettings = {
    /** Whether the SSO (via OIDC) section should be enabled in the Authorize popup */
    enabled: boolean,
    /** The default OIDC provider to pre-configure - must match a key in "AuthSettings.oidc" */
    defaultProvider: string | null,
    /** Whether to automatically start SSO when the Authorize popup model loads */
    autoSso: boolean,
    /** The actually chosen OIDC provider (which can be changed by the user in the frontend) - must match a key in "AuthSettings.oidc" */
    provider?: string
}

type BasicAuthSettings = {
    /** Whether the Basic Auth section should be enabled in the Authorize popup */
    enabled: boolean,
    /** The default username and password to pre-configure */
    defaultUsernamePassword: string | null
}

type BearerAuthSettings = {
    /** Whether the Bearer Auth section should be enabled in the Authorize popup */
    enabled: boolean
}

type PreAuthSettings = {
    /** Whether the Pre-Authenticated section should be enabled in the Authorize popup */
    enabled: boolean,
    /** The pre-authenticated username to pre-configure */
    defaultDittoPreAuthenticatedUsername: string | null,
    /** The cached pre-authenticated username */
    dittoPreAuthenticatedUsername?: string
}
```
An example environment JSON file could look like:
```json
{
  "local_ditto": {
    "api_uri": "http://localhost:8080",
    "ditto_version": 3,
    "disablePolicies": false,
    "disableConnections": false,
    "disableOperations": false,
    "authSettings": {
      "main": {
        "method": "basic",
        "oidc": {
          "enabled": false
        },
        "basic": {
          "enabled": true,
          "defaultUsernamePassword": "ditto:ditto"
        },
        "bearer": {
          "enabled": true
        },
        "pre": {
          "enabled": false,
          "defaultDittoPreAuthenticatedUsername": null
        }
      },
      "devops": {
        "method": "basic",
        "oidc": {
          "enabled": false
        },
        "basic": {
          "enabled": true,
          "defaultUsernamePassword": "devops:foobar"
        },
        "bearer": {
          "enabled": true
        }
      },
      "oidc": {
      }
    }
  },
  "local_ditto_ide": {
    "api_uri": "http://localhost:8080",
    "ditto_version": 3,
    "disablePolicies": false,
    "disableConnections": false,
    "disableOperations": false,
    "authSettings": {
      "main": {
        "method": "pre",
        "oidc": {
          "enabled": false
        },
        "basic": {
          "enabled": true,
          "defaultUsernamePassword": null
        },
        "bearer": {
          "enabled": true
        },
        "pre": {
          "enabled": false,
          "defaultDittoPreAuthenticatedUsername": "pre:ditto"
        }
      },
      "devops": {
        "method": "basic",
        "oidc": {
          "enabled": false
        },
        "basic": {
          "enabled": true,
          "defaultUsernamePassword": "devops:foobar"
        },
        "bearer": {
          "enabled": true
        }
      },
      "oidc": {
      }
    }
  },
  "ditto_sandbox": {
    "api_uri": "https://ditto.eclipseprojects.io",
    "ditto_version": 3,
    "disablePolicies": false,
    "disableConnections": true,
    "disableOperations": true,
    "authSettings": {
      "main": {
        "method": "basic",
        "oidc": {
          "enabled": true,
          "defaultProvider": "fake"
        },
        "basic": {
          "enabled": true,
          "defaultUsernamePassword": "ditto:ditto"
        },
        "bearer": {
          "enabled": true
        },
        "pre": {
          "enabled": false,
          "defaultDittoPreAuthenticatedUsername": null
        }
      },
      "devops": {
        "method": "basic",
        "oidc": {
          "enabled": false,
          "defaultProvider": "fake"
        },
        "basic": {
          "enabled": false,
          "defaultUsernamePassword": null
        },
        "bearer": {
          "enabled": false
        }
      },
      "oidc": {
      }
    }
  },
  "oidc_example": {
    "api_uri": "http://localhost:8080",
    "ditto_version": 3,
    "disablePolicies": false,
    "disableConnections": false,
    "disableOperations": false,
    "authSettings": {
      "main": {
        "method": "oidc",
        "oidc": {
          "enabled": true,
          "defaultProvider": "fake",
          "autoSso": true
        },
        "basic": {
          "enabled": false,
          "defaultUsernamePassword": null
        },
        "bearer": {
          "enabled": true
        },
        "pre": {
          "enabled": false,
          "defaultDittoPreAuthenticatedUsername": null
        }
      },
      "devops": {
        "method": "oidc",
        "oidc": {
          "enabled": true,
          "defaultProvider": "fake",
          "autoSso": true
        },
        "basic": {
          "enabled": false,
          "defaultUsernamePassword": null
        },
        "bearer": {
          "enabled": true
        }
      },
      "oidc": {
        "providers": {
          "fake": {
            "displayName": "Fake IDP to test", 
            "extractBearerTokenFrom": "access_token",
            "authority": "http://localhost:9900/fake",
            "client_id": "some-client-id",
            "redirect_uri": "http://localhost:8000",
            "post_logout_redirect_uri": "http://localhost:8000",
            "response_type": "code",
            "scope": "openid"
          }
        }
      }
    }
  }
}
```

### OpenID Connect configuration
The Ditto UI makes use of the [oidc-client-ts](https://authts.github.io/oidc-client-ts/) library and simply delegates
all OIDC / OAuth2.0 configuration options to the
[UserManager's constructor `settings`](https://authts.github.io/oidc-client-ts/classes/UserManager.html#constructor)
being of type [UserManagerSettings](https://authts.github.io/oidc-client-ts/interfaces/UserManagerSettings.html),
extending [OidcClientSettings](https://authts.github.io/oidc-client-ts/interfaces/OidcClientSettings.html).
Please refer to the [oidc-client-ts](https://authts.github.io/oidc-client-ts/) documentation in order to configure your
OIDC client accordingly as part of your environment's `authSettings.oic.providers.<providerkey>` payload.


## Authorization
To access the REST API of your selected Ditto instance you must provide valid credentials by clicking on "Authorize"