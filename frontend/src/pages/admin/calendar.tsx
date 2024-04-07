import Calendar from "@/components/Calender";
import DefaultLayout from "@/components/Layouts/DefaultLayout";
import useRequireAuth from '@/hooks/useRequireAuth'
import AlertComponent from '@/components/Alert';
import Navbar from '@/components/Navbar';
import Footer from '@/components/Footer';

const CalendarPage = () => {

  const { loading } = useRequireAuth("Administrator");

  if (loading) {
    return <div>Loading...</div>;
  }
  return (
    <>
    <Navbar />
    <AlertComponent />
    <DefaultLayout>
      <Calendar />
    </DefaultLayout>
    <Footer />
    </>
  );
};

export default CalendarPage;
