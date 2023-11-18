import { collections } from './data.js';

export function load() {
	return {
		summaries: collections.map((collection) => ({
			name: collection.name,
			price: collection.price,
			items: collection.items
			
		}))
	};
}
