import MainLayout from "../layouts/MainLayout";

function MyProducts() {
  return (
    <MainLayout>
      <div className="bg-white rounded-2xl border border-slate-200 shadow-sm p-10">

        <h1 className="text-3xl font-bold text-slate-800">
          My Products
        </h1>

        <p className="text-slate-500 mt-3">
          Manage all your tracked products.
        </p>

        <div className="mt-10 text-center text-slate-400">
          🚧 Product management will be available in Sprint 3.
        </div>

      </div>
    </MainLayout>
  );
}

export default MyProducts;