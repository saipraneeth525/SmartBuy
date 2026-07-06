import product from "../../data/product";

function ReviewCard() {
  return (
<div className="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 transition-all duration-300 hover:-translate-y-1 hover:shadow-xl">      <h2 className="text-xl font-semibold text-slate-800">
        Customer Reviews
      </h2>

      <div className="mt-6 flex items-center gap-4">

        <div className="text-5xl">
          ⭐
        </div>

        <div>

          <h3 className="text-3xl font-bold">
            {product.rating}
          </h3>

          <p className="text-slate-500">
            {product.reviews.toLocaleString()} Reviews
          </p>

        </div>

      </div>

      <div className="mt-6">

        <div className="w-full bg-slate-200 rounded-full h-3">
          <div
            className="bg-yellow-400 h-3 rounded-full"
            style={{ width: "92%" }}
          />
        </div>

        <p className="mt-3 text-green-600 font-medium">
          Overall sentiment: Positive
        </p>

      </div>

    </div>
  );
}

export default ReviewCard;