function Inventory() {
  return (
    <div>
        <h2>Inventory</h2>
        <h4>Form</h4>
        <form className="form">
            <label htmlFor="product_name">Product Name:</label>
            <input type="text" id="product_name" placeholder="Product Name" />

            <label htmlFor="brands">Brands:</label>
            <input type="text" id="brands" placeholder="Brands" />

            <label htmlFor="ingredients_text">Ingredients Text:</label>
            <input type="text" id="ingredients_text" placeholder="Ingredients Text" />
            
            <button type="submit">Add Product</button>
        </form>
    </div>
  );
}