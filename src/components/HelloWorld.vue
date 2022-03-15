<template>
  <div class="hello">
    <h2>NSP Books Lookup</h2>
    <input v-model="message" placeholder="Type a tune name">
    <table>
      <!-- <th>
        <td>Tune Name</td>
        <td>Book</td>
        <td>Page</td>
      </th> -->
      <tr v-for="(item) in tuneInfo" v-bind:key="item.key">
        <td>{{ item.tune }}</td>
        <td>{{item.book}}</td>
        <!-- <td>{{item.edition}}</td> -->
        <td>{{item.page}}</td>
      </tr>
    </table>

    <div class="footer">
      🎼 Written by Tim Pillinger
      <br>
      <a href="https://github.com/wxtim/tunebook-companion">Source Code</a>
      🔷
      <a href="https://github.com/wxtim/tunebook-companion/issues">Make a suggestion</a>
      <br>
    </div>
  </div>
</template>

<script>
import {bookData} from "./tunebooks.json";

export default {
  name: 'HelloWorld',
  data: function () {
    return {message: ''}
  },
  computed: {
    tuneInfo: function(message) {
      console.log(message)
      var tunes = [];
      for (let book in bookData) {
        for (let edition in bookData[book]) {
          for (let tune in bookData[book][edition]) {
            console.log(tune)
            if (tune.toLowerCase().match(this.message.toLowerCase())) {
              tunes.push({
                "tune":tune,
                "book":book,
                "edition": edition,
                "page":bookData[book][edition][tune],
                "key": tune + "." + book + "." + edition
              })
            }
            // eslint-disable-next-line
            // debugger
          }
        }
      }
      var tunesize = Object.keys(tunes).length;
      if (tunesize > 12) {
        tunes = []
      }
      return tunes
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  /* list-style-type: none; */
  padding: 0;
}
li {
  /* display: inline-block; */
  margin: 0 10px;
}
a {
  color: #42b983;
}
table {
  padding: 15px;
  border: 1px solid #000;
  border-collapse: collapse;
  margin-top: 10px;
  margin-left: auto;
  margin-right: auto;
  text-align: right;
  border-radius: 5px;
}
td {
  padding: 5px;
  border: 1px solid #000;
  text-align: right;
  border-style: solid;
  border-color: #000;
  border-radius: 5px;
}
input {
  padding: 5px;
  border-radius:5px;
}
.footer {
  position: fixed;
  left: 0;
  bottom: 40px;
  width: 100%;
  text-align: center;
}
.hello {
  background: #a0a5b8;
  border-radius: 5px;
  padding: 10px;
}
</style>
