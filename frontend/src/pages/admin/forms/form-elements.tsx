import React from "react";
import FormElements from "@/components/FormElements";
import { Metadata } from "next";
import DefaultLayout from "@/components/Layouts/DefaultLayout";
import { useRequireAuth } from "@/hooks/useRequireAuth";



const FormElementsPage = () => {
  const { isLoading } = useRequireAuth("Administrator");

  if (isLoading) {
    return <div>Loading...</div>;
  }
  return (
    <DefaultLayout>
      <FormElements />
    </DefaultLayout>
  );
};

export default FormElementsPage;
