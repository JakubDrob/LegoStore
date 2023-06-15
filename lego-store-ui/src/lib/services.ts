import type { Cart, Product } from "./models";

export const getProducts = async () => {
  const result = await fetch("http://legostorebackend.azurewebsites.net/products");
  const products = await result.json();
  return products.products as Product[];
};

export const getCart = async (userId: number) => {
  const result = await fetch(`http://legostorebackend.azurewebsites.net/users/${userId}/cart`);
  const cart = await result.json();
  console.log(cart);
  return cart as Cart;
};

export const decrementCartItem = async (userId: number, productId: number) => {
  const result = await fetch(
    `http://legostorebackend.azurewebsites.net/users/${userId}/cart/${productId}/quantity`,
    { method: "DELETE" }
  );
};

export const incrementCartItem = async (userId: number, productId: number) => {
  const result = await fetch(
    `http://legostorebackend.azurewebsites.net/users/${userId}/cart/${productId}/quantity`,
    { method: "POST" }
  );
};

export const addProductToCart = async (userId: number, productId: number) => {
  const result = await fetch(`http://legostorebackend.azurewebsites.net/users/1/cart`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ productId }),
  });
};
