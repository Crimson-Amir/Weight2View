import '../style.css';
import('preline')
import { createApp } from 'vue';
import { findItem } from './wrapper';

  const app = {
    data() {
      return {
        text: 'Weight2View',
        weight: null,
        itemId: "67a2680d6cf2500e7e74f743",
        svg: null,
        searchIntialized: false,
        loading: false
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
      }
    }
  };

createApp(app).mount('#app');