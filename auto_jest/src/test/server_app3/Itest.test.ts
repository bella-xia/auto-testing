import * as generated from "../../app/server_app/data/IdGenerator";
import { Account } from "../../app/server_app/model/AuthModel";
import { Reservation } from "../../app/server_app/model/ReservationModel";
import {
  HTTP_CODES,
  HTTP_METHODS,
} from "../../app/server_app/model/ServerModel";
import { Server } from "../../app/server_app/server/Server";
import { makeAwesomeRequest } from "./utils/http-client";

xdescribe("Server app integration tests", () => {
  let server: Server;

  beforeAll(() => {
    server = new Server();
    server.startServer();
  });

  afterAll(() => {
    server.stopServer();
  });

  const someUser: Account = {
    id: "",
    userName: "someUserName",
    password: "somePassword",
  };

  const someReservation: Reservation = {
    id: "",
    endDate: "someEndDate",
    startDate: "someStartDate",
    room: "someRoom",
    user: "someUser",
  };

  it("should register new user", async () => {
    const result = await fetch("http://localhost:8080/register", {
      method: HTTP_METHODS.POST,
      body: JSON.stringify(someUser),
    });
    const resultBody = await result.json();

    expect(result.status).toBe(HTTP_CODES.CREATED);
    expect(resultBody.userId).toBeDefined();
    console.log(`connecting in address ${process.env.HOST}`);
  });

  it("should register new user with awesome request", async () => {
    const result = await makeAwesomeRequest(
      {
        host: "localhost",
        port: 8080,
        method: HTTP_METHODS.POST,
        path: "/register",
      },
      someUser
    );
    expect(result.statusCode).toBe(HTTP_CODES.CREATED);
    expect(result.body.userId).toBeDefined();
  });

  let token: string;

  it("should log in new user", async () => {
    const result = await fetch("http://localhost:8080/login", {
      method: HTTP_METHODS.POST,
      body: JSON.stringify(someUser),
    });
    const resultBody = await result.json();

    expect(result.status).toBe(HTTP_CODES.CREATED);
    expect(resultBody.token).toBeDefined();
    token = resultBody.token;
  });

  let reservationId: string;
  it("should create reservation if authorized", async () => {
    const result = await fetch("http://localhost:8080/reservation", {
      method: HTTP_METHODS.POST,
      body: JSON.stringify(someReservation),
      headers: {
        authorization: token,
      },
    });
    const resultBody = await result.json();

    expect(result.status).toBe(HTTP_CODES.CREATED);
    expect(resultBody.reservationId).toBeDefined();
    reservationId = resultBody.reservationId;
  });

  it("should get the corresponding reservation", async () => {
    const result = await fetch(
      `http://localhost:8080/reservation/${reservationId}`,
      {
        method: HTTP_METHODS.GET,
        headers: {
          authorization: token,
        },
      }
    );
    const expectedReservation = structuredClone(someReservation);
    expectedReservation.id = reservationId;
    const resultBody = await result.json();

    expect(result.status).toBe(HTTP_CODES.OK);
    expect(resultBody).toEqual(expectedReservation);
  });

  it("should create and retrieve multiple reservations", async () => {
    await fetch("http://localhost:8080/reservation", {
      method: HTTP_METHODS.POST,
      body: JSON.stringify(someReservation),
      headers: {
        authorization: token,
      },
    });

    await fetch("http://localhost:8080/reservation", {
      method: HTTP_METHODS.POST,
      body: JSON.stringify(someReservation),
      headers: {
        authorization: token,
      },
    });

    await fetch("http://localhost:8080/reservation", {
      method: HTTP_METHODS.POST,
      body: JSON.stringify(someReservation),
      headers: {
        authorization: token,
      },
    });

    const getAllResults = await fetch("http://localhost:8080/reservation/all", {
      method: HTTP_METHODS.GET,
      headers: {
        authorization: token,
      },
    });
    const resultBody = await getAllResults.json();
    expect(getAllResults.status).toBe(HTTP_CODES.OK);
    expect(resultBody).toHaveLength(4);
  });

  it("should update reservation", async () => {
    const result = await fetch(
      `http://localhost:8080/reservation/${reservationId}`,
      {
        method: HTTP_METHODS.PUT,
        body: JSON.stringify({ startDate: "someOtherStateDate" }),
        headers: {
          authorization: token,
        },
      }
    );

    expect(result.status).toBe(HTTP_CODES.OK);

    const getResult = await fetch(
      `http://localhost:8080/reservation/${reservationId}`,
      {
        method: HTTP_METHODS.GET,
        headers: {
          authorization: token,
        },
      }
    );

    const getResultBody: Reservation = await getResult.json();
    expect(getResultBody.startDate).toBe("someOtherStateDate");
  });

  it("should delete reservation", async () => {
    const result = await fetch(
      `http://localhost:8080/reservation/${reservationId}`,
      {
        method: HTTP_METHODS.DELETE,
        headers: {
          authorization: token,
        },
      }
    );

    expect(result.status).toBe(HTTP_CODES.OK);

    const getResult = await fetch(
      `http://localhost:8080/reservation/${reservationId}`,
      {
        method: HTTP_METHODS.GET,
        headers: {
          authorization: token,
        },
      }
    );

    expect(getResult.status).toBe(HTTP_CODES.NOT_fOUND);
  });

  it("snapshot demo", async () => {
    jest.spyOn(generated, "generateRandomId").mockReturnValueOnce("12345");
    await fetch("http://localhost:8080/reservation", {
      method: HTTP_METHODS.POST,
      body: JSON.stringify(someReservation),
      headers: {
        authorization: token,
      },
    });

    const getResult = await fetch("http://localhost:8080/reservation/12345", {
      method: HTTP_METHODS.GET,
      headers: {
        authorization: token,
      },
    });
    const getRequestBosy: Reservation = await getResult.json();

    expect(getRequestBosy).toMatchSnapshot();
  });
});
