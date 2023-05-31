export type Product = {
    name: string,
    image_path: string,
    price: number,
    id: number,
    set_no: string,
}

export type Cart = {
    items: CartItem[] 
}

export type CartItem = {
    productId: number,
    title: string,
    quantity: number,
    image: string,
    price: number
}

