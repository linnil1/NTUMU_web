<template>
  <nav class="navbar navbar-default navbar-fixed-top" id="navbar">
    <div class="container-fluid">
      <div class="navbar-header">
        <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#nav-collapse" aria-expanded="false">
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
        <router-link to="/" class="navbar-brand">
          <img src="static/img/105_1_logo.png"  height="50" alt="logo">
        </router-link>
        <a class="title-word navbar-brand navbar-word">{{$store.state.title}}</a>
      </div>
      <div class="collapse navbar-collapse" id="nav-collapse">
        <ul class="nav navbar-nav"  >
          <!-- Narbar -->
          <li v-for="nav in nav_bar" v-bind:key="nav.url">
            <router-link :to="'/'+ts+nav.url"
              >{{nav.name}}</router-link>
          </li>
          <!-- Club -->
          <li class="dropdown">
            <router-link class="dropdown-toggle"
                         :to="'/'+ts+'/club'">
              {{club}}<b class="caret"></b></router-link>
            <ul class="dropdown-menu grid">
              <li v-for="club in clubs" v-bind:key="club.url">
                <router-link v-bind:to="'/'+ts+club.url">{{club.name}}</router-link>
              </li>
            </ul>
          </li>
        </ul>

        <!-- Version -->
        <ul class="nav navbar-nav navbar-right">
          <li class="dropdown">
            <a class="dropdown-toggle" v-on:click="verClick">
              {{versionname}}: {{ts}}<b class="caret"></b></a>
            <ul class="dropdown-menu ">
              <li v-for="ver in versions" v-bind:key="ver">
                <router-link :to="urlmodify(ver)">{{ver}}</router-link>
              </li>
            </ul>
          </li>
        </ul>
      </div>
    </div>

    <!-- version control for mobile -->
    <div class="verbox"
         v-show="vershow"
         v-on:click= "vershow=false">
      <div class="ver-in">
        <router-link v-for="ver in versions" v-bind:key="ver"
               tag="div"
               :to="urlmodify(ver)">
          <span class="glyphicon glyphicon-menu-right" v-if="ts==ver"></span>
          {{ver}}
        </router-link>
      </div>
    </div>
  </nav>
</template>

<style scoped>
.navbar{
  margin: 0;
}
.navbar ul.grid{
  width: 570px;
}
.navbar ul.grid li{
  padding: 2px ;
  float:left;
}
.navbar ul.grid li a{
  display:block;
  border:none;
}
.navbar-brand img{
  position: relative;
  top:-15px;
  left:-15px;
}
@media only screen and (min-width : 768px) {
    /* Make Navigation Toggle on Desktop Hover */
  .dropdown:hover .dropdown-menu {
    display: block;
  }
  .mobile-hide{
    display: none;
  }
}
@media only screen and (max-width : 768px) {
  .navbar-word{
    display: inline-block;
    position: relative;
    left:-30px;
    padding:inherit 0 inherit 0;
    max-width: calc(100vw - 150px);/* logo 90+ button 45+ padding 30 */
    white-space: nowrap;
    overflow: hidden;
  }
}

.verbox {
//  display: none;
  /** Position and style */
  position: fixed;
  z-index: 999;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  background: rgba(0,0,0,0.8);
  display: flex;
  align-items: center;
  justify-content: center;
}
.ver-in{
  width:80%;
  max-width: 300px;
  background: white;
  border-radius:10px;
}
.ver-in div{
  border-radius:10px;
  border: 1px solid #c5c5c5;
  text-align: center;
  height: 3em;
  color: #333333;
  font-size: 2em;
  display: flex;
  align-items: center;
  justify-content: center;
}
.ver-in div:hover{
  background: #007fff;
  color: #ffffff;
  cursor: pointer;
}

</style>

<script>

export default {
  name: 'navbar',
  // props: ['ver'],
  data () {
    return {
      club: '社團',
      clubs: [],
      versionname: '版本',
      versions: [],
      title: '台大武術聯盟',
      vershow: false
    };
  },
  created: function () {
    // $(".title-word").html(this.title)
    var jsondata = this.$store.state.clubsdata;
    var ts = this.ts;
    this.versions = jsondata.version;
    var clubs = this.clubs;
    jsondata[ts].clubs.forEach(function (club) {
      clubs.push({
        name: jsondata[club].chinese,
        url: '/club/' + club
      });
    });
    document.body.style.paddingTop = '50px';
  },
  mounted: function () {
    // navbar collapse after click
    console.log(document.querySelector('#nav-collapse'));
    document.querySelector('#nav-collapse').addEventListener(
      'click', function (e) {
        if (this.classList.contains('in') && e.target.tagName.toLowerCase() === 'a') {
          this.classList.toggle('in');
        }
        console.log(e);
      });
    /*
    $(document).on('click', '.navbar-collapse.in', function (e) {
      if ($(e.target).is('a')) {
        $('.navbar-collapse').collapse('hide');
      }
    });
    */
  },
  methods: {
    // bad methods to modify version
    urlmodify: function (v) {
      var s = this.$route.path;
      var want = s.slice(s.indexOf('/', 1) + 1);

      // not good methods
      console.log(s);
      if (['showtime', 'countdown', 'boothmap'].indexOf(want) >= 0 &&
        !(want in this.$store.state.clubsdata[v])) { return '/' + v + '/club'; }
      return '/' + v + '/' + want;
    },
    verClick: function (evt) {
      console.log(evt);
      this.vershow = true;
    }
  },
  computed: {
    ts: function () {
      return this.$store.state.ver;
    },
    nav_bar: function () {
      var option = [ {
        name: '攤位',
        url: '/boothmap'
      }, {
        name: '表演節目',
        url: '/showtime'
      }, {
        name: '倒數',
        url: '/countdown'
      }];
      var clubdata = this.$store.state.clubsdata;
      var ts = this.$store.state.ver;

      var newvar = option.filter(function (opt) {
        return opt.url.slice(1) in clubdata[ts];
      });
      newvar.push({
        name: '課表',
        url: '/course'
      });
      return newvar;
    }
  }
};
</script>
