import { TestBed, inject } from '@angular/core/testing';

import { UserFieldGroupService } from './user-field-group.service';

describe('UserFieldGroupService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [UserFieldGroupService]
    });
  });

  it('should be created', inject([UserFieldGroupService], (service: UserFieldGroupService) => {
    expect(service).toBeTruthy();
  }));
});
