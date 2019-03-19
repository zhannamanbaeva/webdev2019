import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FacecareComponent } from './facecare.component';

describe('FacecareComponent', () => {
  let component: FacecareComponent;
  let fixture: ComponentFixture<FacecareComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FacecareComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FacecareComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
