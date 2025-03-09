import '../style.css';
import('preline')
import { createApp } from 'vue';
import { findItem, findItems } from './wrapper';
import { debounce } from 'lodash';
import axios from 'axios';


  let abortController = new AbortController();

  const app = {
    data() {
      return {
        text: 'Weight2View',
        weight: null,
        itemId: "67a2680d6cf2500e7e74f743",
        svg: null,
        searchIntialized: false,
        loading: false,
        searchText: "",
        searchItems: ['ali'],
        debouncedSearch: debounce(() => {}, 300)
      }
    },
    methods: {
      async findingItem(){
        this.loading = true
        this.svg = await findItem(this.weight, this.itemId)
        if(this.svg)
        {
          this.searchIntialized = true
        }
        else
        {
          this.searchIntialized = false
        }
        this.loading = false
      },
      reset(){
        this.weight = null
        this.itemId = null
        this.svg = null
        this.searchIntialized = false
        this.loading = false
      },
      async search(){

        if (abortController instanceof AbortController) {
          setTimeout(() => abortController.abort(), 50);
        }

        abortController = new AbortController()

        if(this.searchText.length > 2)
        {
          axios.post(import.meta.env.VITE_DB_URL+"find_items",{
            item_name: this.searchText,
            top_number: parseFloat(10)
          })
          .then((res) => {
            //  this.searchItems = Array.isArray(res.data.items) ? res.data.items : [];
            //  console.log(this.searchItems)
            //this.searchItems = ['ali']
            })
        }
      }
    },
    watch: {
      searchText(newQuery){
        this.debouncedSearch(newQuery)
      }
    },
    created() {
      this.debouncedSearch = debounce(this.search, 300);
    }
  };

createApp(app).mount('#app');