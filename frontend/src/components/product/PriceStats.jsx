import product from "../../data/product";

function PriceStats() {
  const stats = [
    {
      title: "Current Price",
      value: product.currentPrice,
      color: "text-violet-600",
    },
    {
      title: "Lowest Price",
      value: product.lowestPrice,
      color: "text-green-600",
    },
    {
      title: "Average Price",
      value: product.averagePrice,
      color: "text-blue-600",
    },
    {
      title: "Highest Price",
      value: product.highestPrice,
      color: "text-red-600",
    },
  ];

  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-4 gap-5">
      {stats.map((stat) => (
        <div
          key={stat.title}
          className="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 transition-all duration-300 hover:-translate-y-1 hover:shadow-xl"
        >
          <p className="text-slate-500 text-sm">
            {stat.title}
          </p>

          <h2 className={`text-3xl font-bold mt-3 ${stat.color}`}>
            ₹{stat.value.toLocaleString()}
          </h2>
        </div>
      ))}
    </div>
  );
}

export default PriceStats;