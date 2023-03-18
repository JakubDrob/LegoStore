CREATE TABLE lego_store;

use lego_store;

CREATE TABLE `ProductType` (
  `ProductTypeID` Int AUTO_INCREMENT,
  `Name` varchar(50),
  PRIMARY KEY (`ProductTypeID`)
);

CREATE TABLE `Product` (
  `ProductID` int AUTO_INCREMENT,
  `Name` varchar(50),
  `SetNo` varchar(50),
  `Price` varchar(50),
  `Description` varchar(250),
  `Image` BLOB,
  `Availability` Int,
  `ReleaseDate` Date,
  `PieceCount` Int,
  `ProductTypeID` Int,
  PRIMARY KEY (`ProductID`),
  FOREIGN KEY (`ProductTypeID`) REFERENCES `ProductType`(`ProductTypeID`)
);

CREATE TABLE `Set` (
  `SetID` int AUTO_INCREMENT,
  `Name` varchar(50),
  `SetNo` varchar(50),
  `Price` varchar(50),
  `Description` varchar(250),
  `Image` BLOB,
  `Availibility` Int,
  `UnitsSold` Int,
  `ReleaseDate` Date,
  `PieceCount` Int,
  `Instruction` text,
  PRIMARY KEY (`SetID`)
);

CREATE TABLE `ShoppingCart` (
  `ShoppingCartID` Int AUTO_INCREMENT,
  `ShippingCost` Int,
  `NumberOfItems` Int,
  `TotalPrice` Int,
  PRIMARY KEY (`ShoppingCartID`)
);

CREATE TABLE `User` (
  `UserID` Int AUTO_INCREMENT,
  `Username` varchar(50),
  `Email` varchar(50),
  `Password` varchar(50),
  `ShoppingCartID` Int,
  `Address` Int,
  PRIMARY KEY (`UserID`)
);

CREATE TABLE `Address` (
  `AddressID` Int AUTO_INCREMENT,
  `FirstName` varchar(50),
  `LastName` varchar(50),
  `Country` varchar(50),
  `City` varchar(50),
  `StreetName` varchar(50),
  `StreetNo` Int,
  `AppartmentNo` varchar(10),
  `PostCode` Int,
  PRIMARY KEY (`AddressID`)
);

CREATE TABLE `ShoppingCart_Product` (
  `ShoppingCartProductID` Int AUTO_INCREMENT,
  `ShoppingCartID` Int,
  `ProductID` Int,
  `SetID` Int,
  PRIMARY KEY (`ShoppingCartProductID`),
  FOREIGN KEY (`ShoppingCartID`) REFERENCES `ShoppingCart`(`ShoppingCartID`),
  FOREIGN KEY (`ProductID`) REFERENCES `Product`(`ProductID`),
  FOREIGN KEY (`SetID`) REFERENCES `Set`(`SetID`),
  CHECK (`ProductID` IS NOT NULL OR `SetID` IS NOT NULL)
);

CREATE TABLE `Set_Product` (
  `SetProductID` Int AUTO_INCREMENT,
  `SetID` Int,
  `ProductID` Int,
  PRIMARY KEY (`SetProductID`),
  FOREIGN KEY (`ProductID`) REFERENCES `Product`(`ProductID`),
  FOREIGN KEY (`SetID`) REFERENCES `Set`(`SetID`)
);

CREATE TABLE `BuyingHistory` (
  `BuyingHistoryID` Int AUTO_INCREMENT,
  `UserID` Int,
  `ShoppingCartID` Int,
  `DateOfPurchase` Date,
  PRIMARY KEY (`BuyingHistoryID`),
  FOREIGN KEY (`UserID`) REFERENCES `User`(`UserID`)
);
