import product from "../../data/product";

function ProductCard() {
  return (
<div  className="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 transition-all duration-300 hover:-translate-y-1 hover:shadow-xl">
      <div className="flex gap-6">

        <img
          src={product.image}
          alt={product.name}
          className="rounded-xl hover:scale-105 transition-all duration-300"
        />

        <div className="flex flex-col justify-center">

          <h2 className="text-3xl font-bold text-slate-800">
            {product.name}
          </h2>

          <p className="text-slate-500 mt-2">
            {product.brand}
          </p>

          <p className="mt-4">
            ⭐ {product.rating}
            {" "}
            ({product.reviews.toLocaleString()} Reviews)
          </p>

          <p className="mt-2">
            Store: <strong>{product.store}</strong>
          </p>

          <p className="mt-2 text-green-600 font-semibold">
            {product.availability}
          </p>

        </div>

      </div>

    </div>
  );
}

export default ProductCard;