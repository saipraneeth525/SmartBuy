import { PackageSearch } from "lucide-react";

function EmptyState() {
  return (
    <section className="mt-8 bg-white border border-slate-200 rounded-2xl p-12 text-center">

      <div className="flex justify-center mb-5">
        <div className="bg-violet-100 p-5 rounded-full">
          <PackageSearch
            size={42}
            className="text-violet-600"
          />
        </div>
      </div>

      <h2 className="text-2xl font-semibold text-slate-800">
        No Products Tracked Yet
      </h2>

      <p className="mt-3 text-slate-500 max-w-lg mx-auto">
        Start by analyzing your first Amazon or Flipkart product.
        SmartBuy will monitor its price, analyze historical trends,
        and notify you when it's the best time to buy.
      </p>

    </section>
  );
}

export default EmptyState;