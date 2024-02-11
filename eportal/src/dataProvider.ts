
// const restProvider = simpleRestProvider('http://192.168.1.51:5008');

import { DataProvider, DeleteManyParams, DeleteManyResult, DeleteParams, DeleteResult, GetManyParams, GetManyReferenceParams, GetManyReferenceResult, GetManyResult, Identifier, RaRecord, UpdateManyParams, UpdateManyResult, UpdateParams, UpdateResult, fetchUtils } from 'ra-core';
import { CreateParams, CreateResult } from 'react-admin';

const httpClient = fetchUtils.fetchJson;
const apiUrl =  'http://192.168.1.51:5008';
//const apiUrl = process.env.VITE_JSON_SERVER_URL;


const myDataProvider: DataProvider = {
  getList: async (resource, params) => {
    const { page, perPage } = params.pagination;
    const { field, order } = params.sort;
    const query = {
      sort: JSON.stringify([field, order]),
      range: JSON.stringify([(page - 1) * perPage, page * perPage - 1]),
      filter: JSON.stringify(params.filter),
    };
    const url = `${apiUrl}/${resource}?${fetchUtils.queryParameters(query)}`;

    const { headers, json } = await httpClient(url);
    return ({
      data: json,
      total: parseInt(headers.get('content-range')?.split('/').pop() || '0', 10),
    });
  },
  getOne: (resource, params) => 
  httpClient(`${apiUrl}/${resource}/${encodeURIComponent(params.id)}`)
    .then(({ json }) => ({
      data: json,
    })),

  // getOne: (resource, params) => httpClient(`${'http://192.168.1.51:5008'}/${resource}/${params.id}`).then(({ json }) => ({
  //   data: json,
  // })),
  getMany: function <RecordType extends RaRecord<Identifier> = any>(resource: string, params: GetManyParams): Promise<GetManyResult<RecordType>> {
    throw new Error('Function not implemented.');
  },
  getManyReference: function <RecordType extends RaRecord<Identifier> = any>(resource: string, params: GetManyReferenceParams): Promise<GetManyReferenceResult<RecordType>> {
    throw new Error('Function not implemented.');
  },
  update: async function <RecordType extends RaRecord<Identifier> = any>(
    resource: string, 
    params: UpdateParams<any>
): Promise<UpdateResult<RecordType>> {
    // Construct the URL
    const url = `${apiUrl}/${resource}`;
    //const url = `http://localhost:5008/${resource}`;
    // Make the HTTP PUT request
   // print(JSON.stringify(params.data))
    const response = await fetch(url, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(params.data),
    });

    // Check if the request was successful
    if (!response.ok) {
        throw new Error(`Error: ${response.statusText}`);
    }

    // Parse the response
    const data = await response.json();

    // Return the update result
    return {
        data: { ...data, id: params.id },
    };
  },
  // update: function <RecordType extends RaRecord<Identifier> = any>(resource: string, params: UpdateParams<any>): Promise<UpdateResult<RecordType>> {
  //   throw new Error('Function not implemented.');
  // },
  updateMany: function <RecordType extends RaRecord<Identifier> = any>(resource: string, params: UpdateManyParams<any>): Promise<UpdateManyResult<RecordType>> {
    throw new Error('Function not implemented.');
  },
  // create: function <RecordType extends Omit<RaRecord<Identifier>, 'id'> = any, ResultRecordType extends RaRecord<Identifier> = RecordType & { id: Identifier; }>(resource: string, params: CreateParams<any>): Promise<CreateResult<ResultRecordType>> {
  //   throw new Error('Function not implemented.');
  // },
  create: async function <RecordType extends Omit<RaRecord<Identifier>, 'id'> = any, 
                       ResultRecordType extends RaRecord<Identifier> = RecordType & { id: Identifier; }>
                       (resource: string, params: CreateParams<any>): Promise<CreateResult<ResultRecordType>> {
    // Construct the URL
    // const url = `http://localhost:5008/${resource}`;
    //const url = `http://localhost:5008/${resource}`;
    const url = `${apiUrl}/${resource}`;
    // Make the HTTP PUT request
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(params.data),
    });

    // Check if the request was successful
    if (!response.ok) {
        throw new Error(`Error: ${response.statusText}`);
    }

    const data: ResultRecordType = await response.json();

    return { data };
    
    // Parse the response
    // const data = await response.json();

    // // Return the update result
    // return {
    //     data: { ...data, id: params.id },
    // };
  },
  delete: function <RecordType extends RaRecord<Identifier> = any>(resource: string, params: DeleteParams<RecordType>): Promise<DeleteResult<RecordType>> {
    throw new Error('Function not implemented.');
  },
  deleteMany: function <RecordType extends RaRecord<Identifier> = any>(resource: string, params: DeleteManyParams<RecordType>): Promise<DeleteManyResult<RecordType>> {
    throw new Error('Function not implemented.');
  }
};

export default myDataProvider;




// const delayedDataProvider = new Proxy(restProvider, {
//     get: (target, name, self) =>
    
//         name === 'then'
//             ? self
//             : (resource: string, params: any) => {
//                 // URL encode the 'id' parameter if it exists
//                 if (params.id) {
//                     params.id = encodeURIComponent(params.id);
//                 }

//                 // For 'getOne', directly call restProvider.getOne without delay
//                 if (name === 'getOne') {
//                     return restProvider.getOne(resource, params);
//                 }

//                 // For other methods, apply the delay
//                 return new Promise(resolve =>
//                     setTimeout(
//                         () => resolve(restProvider[name as string](resource, params)),
//                         500
//                     )
//                 );
//             },
// });

// export default delayedDataProvider;


// // import jsonServerProvider from "ra-data-json-server";

// // export const dataProvider = jsonServerProvider(
// //   import.meta.env.VITE_JSON_SERVER_URL
  
// // );

// import simpleRestProvider from 'ra-data-simple-rest';

// const restProvider = simpleRestProvider('http://192.168.0.136:5008');

// // const delayedDataProvider = new Proxy(restProvider, {
// //     get: (target, name, self) =>
// //         name === 'then' // as we await for the dataProvider, JS calls then on it. We must trap that call or else the dataProvider will be called with the then method
// //             ? self
// //             : (resource: string, params: any) =>
// //                   new Promise(resolve =>
// //                       setTimeout(
// //                           () =>
// //                               resolve(
// //                                   restProvider[name as string](resource, params)
// //                               ),
// //                           500
// //                       )
// //                   ),
// // });

// const delayedDataProvider = new Proxy(restProvider, {
//   get: (target, name, self) =>
//       name === 'then'
//           ? self
//           : (resource: string, params: any) => {
//               // Modify params here if needed, e.g., URL encode IDs
//               if (params.id) {
//                   params.id = encodeURIComponent(params.id);
//               }

//               // You can add more encoding logic if needed

//               return new Promise(resolve =>
//                   setTimeout(
//                       () =>
//                           resolve(
//                               restProvider[name as string](resource, params)
//                           ),
//                       500
//                   )
//               );
//           },
// });




// export default delayedDataProvider;