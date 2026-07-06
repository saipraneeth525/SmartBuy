import { Link } from "react-router-dom";

function Login() {
  return (
    <div className="min-h-screen bg-slate-100 flex items-center justify-center px-6">
      <div className="w-full max-w-md bg-white rounded-3xl shadow-lg border border-slate-200 p-10">

        <h1 className="text-4xl font-bold text-center text-violet-600">
          SmartBuy
        </h1>

        <p className="text-center text-slate-500 mt-3">
          Welcome back! Sign in to continue.
        </p>

        <form className="mt-10 space-y-5">

          {/* Email */}
          <div>
            <label className="text-sm font-medium">
              Email
            </label>

            <input
              type="email"
              placeholder="Enter your email"
              className="w-full mt-2 border border-slate-300 rounded-xl px-4 py-3 outline-none transition-all focus:ring-2 focus:ring-violet-500"
            />
          </div>

          {/* Password */}
          <div>
            <label className="text-sm font-medium">
              Password
            </label>

            <input
              type="password"
              placeholder="Enter your password"
              className="w-full mt-2 border border-slate-300 rounded-xl px-4 py-3 outline-none transition-all focus:ring-2 focus:ring-violet-500"
            />
          </div>

          {/* Sign In Button */}
          <button
            type="submit"
            className="w-full bg-violet-600 hover:bg-violet-700 hover:scale-[1.02] transition-all duration-300 text-white py-3 rounded-xl font-semibold shadow-md hover:shadow-lg"
          >
            Sign In
          </button>

        </form>

        <p className="text-center mt-8 text-slate-500">
          Don't have an account?{" "}
          <Link
            to="/register"
            className="text-violet-600 font-semibold hover:underline"
          >
            Create Account
          </Link>
        </p>

      </div>
    </div>
  );
}

export default Login;