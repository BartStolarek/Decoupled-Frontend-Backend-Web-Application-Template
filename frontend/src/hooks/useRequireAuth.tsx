// hooks/useRequireAuth.tsx
import { useEffect, useState } from "react";
import { useRouter } from "next/router";
import { useAuth } from "@/contexts/AuthContext";
import { useAlert } from "@/contexts/AlertContext";

type Role = "Administrator" | "User";

const useRequireAuth = (requiredRole: Role) => {
  const { isAuthenticated, loading } = useAuth();
  const { showAlert } = useAlert();
  const router = useRouter();
  const [redirectInitiated, setRedirectInitiated] = useState(false);

  useEffect(() => {
    if (!loading && !redirectInitiated) {
      const role = localStorage.getItem("user_role");
      // For now, assume that the presence of "user_role" in localStorage is enough to validate a role
      // You might want to implement a more secure method to validate roles

      // Check if user is not authenticated or does not have the required role
      if (!isAuthenticated || role !== requiredRole) {
        const alertMessage = requiredRole === "Administrator"
          ? "You are not authorized to access this page. Please login with an Administrator account."
          : "You are not authorized to access this page. Please login.";
        showAlert("Unauthorized", alertMessage, "error", "/", 5000);
        setRedirectInitiated(true); // Prevent further redirects
        // Optional: Redirect to login or home page
        // router.push('/login');
      }
    }
  }, [isAuthenticated, loading, router, showAlert, redirectInitiated, requiredRole]);

  // Placeholder for user auth function
  // TODO: Implement user authentication logic here if needed

  return {
    isAuthenticated,
    loading,
    redirectInitiated,
  };
};

export default useRequireAuth;
