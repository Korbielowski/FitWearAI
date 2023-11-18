<script>
    import { collections } from './data.js';

  export let data;

  let selectedCollection = ""; // Initialize selectedCollection

  function updatePrice(event) {
    selectedCollection = event.target.value;
    selectedCollection = event.target.value;
  selectedCollectionData = data.summaries.find(item => item.name === selectedCollection);


    
  }

  $: selectedCollectionData = data.summaries.find(item => item.name === selectedCollection); // Get selected collection data


  $: price = selectedCollectionData ? selectedCollectionData.price : 0; // Set price based on selected collection

</script>


<div class=" my-4 max-w-screen-md mx-auto p-5">
  <div class="text-center mb-16">
    <p class="mt-4 text-sm leading-7 text-gray-500 font-regular uppercase">
        Collection
      </p>
      <h3 class="text-3xl sm:text-4xl leading-normal font-extrabold tracking-tight text-gray-900">
        Create <span class="text-indigo-600">Collection</span>
      </h3>
  </div>
  

  <div class="flex flex-wrap">
  <form class="w-full md:w-1/2">
  <div class="flex flex-col -mx-3 mb-6">
    <div class="w-full px-3 mb-6 md:mb-0">
      <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="grid-first-name">
        Choose Collection
      </label>

      <form class="w-full">
        <fieldset>
        <div class="relative border border-gray-300 text-gray-800 bg-white">
          <label for="frm-whatever" class="sr-only">My field</label>
          <select class="appearance-none w-full py-1 px-2 bg-white" name="whatever" id="frm-whatever" on:change={updatePrice}>
              <option value="">Please choose&hellip;</option>
              {#each data.summaries as { name, price }}
              <option value={name}>{name}</option>
              {/each}
          </select>
          <div class="pointer-events-none absolute right-0 top-0 bottom-0 flex items-center px-2 text-gray-700 border-l">
              <svg class="h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                  <path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z" />
              </svg>
          </div>
      </div>
          </fieldset>
      </form>
      
      <!-- <p class="text-red-500 text-xs italic">Please fill out this field.</p> -->
    </div>
    <div class="w-full px-3 mt-4 mb-4">
      <p class="text-2xl text-center">Price: <b>{price} PLN</b></p>
    </div>

    <div class="flex justify-center w-full px-3 mt-3">
      {#if selectedCollectionData}
        {#each selectedCollectionData.items as item}
          <div class="w-1/3 h-24 mr-3 bg-gray-200">
            <img src={item} alt={item} class="w-full h-full object-cover">
          </div>
        {/each}
      {/if}
    </div>

    <div class="flex justify-start  w-full px-3 mt-3">
      <div class="md:flex md:items-center">
      </div>
      <button class="shadow mr-3 bg-emerald-600 hover:bg-emerald-400 focus:shadow-outline focus:outline-none text-white font-bold py-2 px-6 rounded" type="submit">
        Save
      </button>
    </div>

  </div>
  </form>

  <div class="w-full md:w-1/2">
    <img src="/avatar2.png" alt="">
  </div>

</div>
</div>


