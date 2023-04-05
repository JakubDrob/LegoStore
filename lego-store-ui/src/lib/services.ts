import type { Product } from "./models";


export const getProducts = async () => {
    const result = await fetch("http://127.0.0.1:5000/products");
    const products = await result.json();
    return products.products as Product[];
}