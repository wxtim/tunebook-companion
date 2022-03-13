<template>
  <div class="hello">
    <h1>NSP Books Lookup</h1>
    <input v-model="message" placeholder="edit me">
    <ul>
      <li v-for="(item) in tuneInfo" v-bind:key="item.tune">
        {{ item.tune }}, {{item.book}}, {{item.edition}}, {{item.page}}
    </li>
    </ul>
  </div>
</template>

<script>
import {bookData} from "./test.json";

export default {
  name: 'HelloWorld',
  data: function () {
    return {message: ''}
  },
  computed: {
    tuneInfo: function(message) {

      console.log(message)
      console.log(bookData)

      var tunes = [];
      for (let book in bookData) {
        for (let edition in bookData[book]) {
          for (let tune in bookData[book][edition]) {
            console.log(tune)
            if (tune.toLowerCase().match(this.message.toLowerCase())) {
              tunes.push({"tune":tune, "book":book, "edition": edition, "page":bookData[book][edition][tune]})
            }
            // eslint-disable-next-line
            // debugger
          }
        }
      }
      console.log(tunes)
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
</style>
