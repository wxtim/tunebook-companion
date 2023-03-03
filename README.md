# Northumbrian Piping Tunebook Directory

**[Go to the tunebook lookup page](https://wxtim.github.io/tunebook-companion/)**

An app designed to take a tune name and return
location of tune in the specific editions of a
tunebook owned by a given user.


# Currently Supported Tunebooks

#### Bewick
  - Probably 3rd (2010) edition - data from J Say
#### Billy Pigg's Compositions
  - Unknown Edition, data from J Say
#### Billy Pigg's Repertoire
  - Unknown Edition, data from J Say
#### Border Minstrel
  - 1
#### Charlton MTB
  - Matches my ancient 1956 edition! Data from J Say
#### Continuing the Tradition
  - Unknown Edition, data from J Say
#### Duet
  - 1
#### Folio 2005
  - Unknown Edition, data from J Say
#### Folio 2007
  - Unknown Edition, data from J Say
#### Folio 2009
  - Unknown Edition, data from J Say
#### Folio 2011
  - Unknown Edition, data from J Say
#### Green Book
  - Unknown Edition, data from J Say
#### James Hill
  - Unknown Edition, data from J Say
#### Minstrelsy
  - Unknown Edition, data from J Say
#### NPS Book 1
  - Unknown Edition, data from J Say
  - 3
#### NPS Book 2
  - Unknown Edition, data from J Say
  - 3
#### NPS Book 3
  - 2
#### NPS Book 4
  - 1
#### Peacock
  - Unknown Edition, data from J Say
#### Yellow Book
  - 3
#### First 30
  - 2008
#### Remember Me
  - 1995
#### Over To You
  - 2015: Many thanks to Philip Howard for data
    inputting.
#### Clough Family Tunebook
  - 2012: Many thanks to Philip Howard for data
    inputting.


# Roadmap

- [x] Build a proof of concept with simple test data
- [x] Deploy PoC on GH pages using GH actions
      to build the project. - this should make the
      deployment repeatable.
- [x] Add backend data to produce a basic app.
- [ ] Add a means to save user preferences about
      which tune books they have.
- [ ] Add an I'm feeling lucky.
- [ ] Add links to folktunefinder and/or the session
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

### Deploy
```
yarn deploy
```
