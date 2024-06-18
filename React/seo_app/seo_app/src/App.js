import React , {useState, useEffect} from 'react'
import api from './api'

const App=()=>{
  const [equipaments, setEquipaments]= useState([]);
  const fetchEquipament= async () => {
    const response=await api.get('/equipament/');
    setEquipaments(response.data)
  };
  useEffect(()=> {
    fetchEquipament();
  },[] );

  return (
    <div>
    <table  className='table table-striped table-bordered table-hover'>
    <thead>
      <tr>
        <th>name</th>
        <th>avr-h</th>
        <th>kwh</th>
        

      </tr>
    </thead>
    <tbody>
      {equipaments.map((equipaments) => (
        <tr key={equipaments.id}>
          <td>{equipaments.name}</td>
          <td>{equipaments.avr_hours}</td>
          <td>{equipaments.kwh}</td>
        </tr>
      ))}
    </tbody>

    </table>

  </div>

  )

}


export default App;
