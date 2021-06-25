import {Route, Switch } from 'react-router-dom';
import IndexPage from './pages/IndexPage';
import SemestersPage from './pages/SemestersPage';
import GpaCalculatePage from './pages/GpaCalculatePage';
import NavBar from './components/NavBar';
import NotFoundPage from './pages/NotFoundPage';

function App() {
  return (
    <>
      <NavBar />
      <Switch>
        <Route path="/:deptid/sem/:semid" exact={true}>
          <GpaCalculatePage />
        </Route>
        <Route path="/:deptid" exact={true}>
          <SemestersPage />
        </Route>
        <Route path="/" exact={true}>
          <IndexPage/>
        </Route>
        <Route path="/*">
          <NotFoundPage/>
        </Route>
      </Switch>
      <div className="d-flex mb-5 justify-content-center text-light">
        Icons from{" "}
        <a className="ms-2" target="_blank" href="https://www.flaticon.com/" title="Flaticon" rel="noreferrer" >
          www.flaticon.com
        </a>
      </div>
    </>
  );
}

export default App;
