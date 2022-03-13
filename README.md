# Northumbrian Piping Tunebook Directory

TODO - add link to github.io page here.

An app designed to take a tune name and return
location of tune in the specific editions of a
tunebook owned by a given user.


# Roadmap

1. Build a proof of concept with simple test data.
2. Deploy PoC on GH pages using GH actions
   to build the project. - this should make the
   deployment repeatable.
3. Add backend data to produce a basic app.
4. Add a means to save user preferences about
   which tune books they have.
5. Add an I'm feeling lucky.
6. Add links to foltunefinder and/or the session
   if tune exists but not in an edition you own.


## Desired appearance:

```
Tune Name:

Find this tune at:
    - Location
    - Location

I have the following tunebooks
Book 1  <dropdown selecting edition or None>
Book 2  <dropdown selecting edition or None>
Book 3  <dropdown selecting edition or None>
Book 4  <dropdown selecting edition or None>
Yellow Book  <dropdown selecting edition or None>
Green Book  <dropdown selecting edition or None>
Duet Book  <dropdown selecting edition or None>
&c &c
```

# Developer information

## Project setup
```
yarn install
```

### Compiles and hot-reloads for development
```
yarn serve
```

### Compiles and minifies for production
```
yarn build
```

### Lints and fixes files
```
yarn lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
