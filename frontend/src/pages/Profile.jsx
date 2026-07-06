import MainLayout from "../layouts/MainLayout";

function Profile() {
  return (
    <MainLayout>
      <div className="bg-white rounded-2xl border border-slate-200 p-10 shadow-sm">
        <h1 className="text-3xl font-bold text-slate-800">
          Profile
        </h1>

        <p className="text-slate-500 mt-3">
          Manage your account information.
        </p>

        <div className="mt-10 text-center text-slate-400">
          🚧 This page will be available in Sprint 3.
        </div>
      </div>
    </MainLayout>
  );
}

export default Profile;