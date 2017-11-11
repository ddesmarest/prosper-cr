import { AuthenticationInfo } from '../authentification.service';
export class FakeAuthentificationService {

    public authInfo: AuthenticationInfo = {
        token: '2345',
        user: {
            email: 'john@test.com',
            first_name: 'John',
            last_name: 'Doe',
            id: '1'
        }
    };

}