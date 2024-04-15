import Calendar from "@/components/Calender";
import DefaultLayout from "@/components/Layouts/DefaultLayout";
import { useRequireAuth } from '@/hooks/useRequireAuth'
import Navbar from '@/components/Navbar';
import Footer from '@/components/Footer';

const CalendarPage = () => {

  const { isLoading } = useRequireAuth("Administrator");

  if (isLoading) {
    return <div>Loading...</div>;
  }
  return (
    <>
    <Navbar />
    <DefaultLayout>
      <Calendar />
    </DefaultLayout>
    <Footer />
    </>
  );
};

export default CalendarPage;
