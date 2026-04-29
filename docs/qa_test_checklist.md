# QA Test Checklist

Use this checklist to validate the hybrid assistant before portfolio delivery.

## Test Cases

| ID | Question | Expected Route | Expected Answer (High Level) | Actual Result | Bug / Notes |
|---|---|---|---|---|---|
| 1 | Quels sont les delais de livraison ? | support | mention 24-48h preparation and 3-5 business days for standard delivery | Les frais de livraison standard sont calculés au moment du paiement selon l’adresse et le mode de livraison choisi. Les frais de livraison express ne sont pas offerts. La livraison standard est offerte à partir de 80 euros d’achat en France métropolitaine. | Wrong FAQ section retrieved: talks about shipping fees instead of delivery timeline. Support answer quality issue. |

| 2 | Quels sont les frais de livraison ? | support | mention calculated shipping fees, free standard delivery from 80 EUR, express not free | Les frais de livraison standard sont calculés au moment du paiement selon l’adresse et le mode de livraison choisi | Partially correct but incomplete: missing free delivery from 80 EUR and express not free. |

| 3 | Puis-je retourner un article solde ? | support | mention discounted items can be returned unless marked final sale / non-returnable | Si le client souhaite une autre taille ou une autre couleur, il doit retourner l’article initial puis passer une nouvelle commande. Les articles soldés pecan être retournés dans les mêmes conditions que les autres articles. Les articles retournés doivent être non portés, non lavés, non endommagés et renvoyés dans leur emballage d’origine. Dans ce cas, les frais de retour sont pris en charge par la boutique.| Mostly correct but polluted by unrelated return/exchange details. Support answer quality issue. |

| 4 | Sous combien de temps suis-je rembourse ? | support | mention refund after return validation in 5-10 business days | Une fois le retour reçu et contrôlé, le remboursement est effectué sous 5 à 10 jours ouvrés. Le suivi peut prendre quelques heures avant d’être mis à jour sur le site du transporteur. Suivi de commande Dans ce cas, les frais de retour sont pris en charge par la boutique. | OK |

| 5 | Comment suivre ma commande ? | support | mention shipping email and tracking link | Le client peut créer un compte pour suivre ses commandes, enregistrer ses adresses et consulter son historique d'achat. | OK |

| 6 | Puis-je annuler une commande deja expediee ? | support | mention cancellation only before preparation / shipping | Une fois la commande expédiée, il n’est plus possible de l’annuler et le client devra passer par une demande de retour après réception. Une commande peut être annulée uniquement si elle n’a pas encore été préparée ou expédiée. Dès qu’une commande est expédiée, un email contenant un lien de suivi est envoyé au client. | Mostly correct but includes extra unrelated tracking sentence. |

| 7 | Que faire si mon article est defectueux ? | support | mention contacting support within 48h and return paid by store | Si un article est reçu défectueux ou incorrect, le client doit contacter le service client dans un délai de 48 heures après réception. Les articles soldés peuvent être retournés dans les mêmes conditions que les autres articles. Si une taille ou une couleur n’apparaît plus, cela signifie généralement que l’article est en rupture de stock. | Partially correct but includes unrelated sold items / stock details. |

| 8 | Quels moyens de paiement acceptez-vous ? | support | mention Visa, Mastercard, Amex, PayPal, Apple Pay | Visa, Mastercard et American Express, plus PayPal et Apple Pay | Correct overall, only wording cleanup needed. |

| 9 | Est-ce que le paiement en plusieurs fois est disponible ? | support | mention not available | Toutes les transactions sont sécurisées. Le paiement en plusieurs fois n’est disponible pour le moment. Les tailles disponibles sont indiquéesdirectement sur la fiche produit. Il est recommandé de joindre des photos de la produit concerned afin de faciliter le traitement de la demande. Tailles et disponibilité | Correct core fact but badly polluted by unrelated content. Support answer quality issue. |

| 10 | Avez-vous des sneakers noires en 42 ? | catalog | return Running Sneakers size 42 in stock | J'ai trouve les produits suivants :
- Running Sneakers | categorie: sneakers | couleur: black | taille: 42 | prix: 89.99 EUR | stock: 10 | OK |

| 11 | et en 43 ? | catalog | preserve previous product context and return size 43 | J'ai trouve les produits suivants :
- Running Sneakers | categorie: sneakers | couleur: black | taille: 43 | prix: 89.99 EUR | stock: 3 | OK - follow-up memory works |

| 12 | Je cherche un hoodie blanc | catalog | return White Oversized Hoodie | J'ai trouve les produits suivants :
- White Oversized Hoodie | categorie: hoodie | couleur: white | taille: M | prix: 54.99 EUR | stock: 14
- White Oversized Hoodie | categorie: hoodie | couleur: white | taille: L | prix: 54.99 EUR | stock: 6| French color parsing || OK |

| 13 | Montre-moi des jeans noirs pour femme | catalog | return High Waist Black Jeans | J'ai trouve les produits suivants :
- High Waist Black Jeans | categorie: jeans | couleur: black | taille: 36 | prix: 64.99 EUR | stock: 11 | French color + gender | | OK |

| 14 | Quels produits a moins de 60 euros ? | catalog | return multiple products priced <= 60 EUR | J'ai trouve les produits suivants :
- Essential Black T-Shirt | categorie: t-shirt | couleur: black | taille: M | prix: 24.99 EUR | stock: 15
- Essential Black T-Shirt | categorie: t-shirt | couleur: black | taille: L | prix: 24.99 EUR | stock: 8
- Thermal Base Layer | categorie: top | couleur: grey | taille: M | prix: 27.99 EUR | stock: 16
- Thermal Base Layer | categorie: top | couleur: grey | taille: L | prix: 27.99 EUR | stock: 9
- Relaxed Fit Shorts | categorie: shorts | couleur: beige | taille: M | prix: 29.99 EUR | stock: 12 | max price parsing | | OK |

| 15 | Avez-vous des bottes marron en 39 ? | catalog | return Leather Chelsea Boots size 39 | J'ai trouve les produits suivants :
- Leather Chelsea Boots | categorie: boots | couleur: brown | taille: 39 | prix: 119.99 EUR | stock: 1 | | OK |

| 16 | Je cherche un manteau beige pour femme | catalog | ideally return Beige Trench Coat | J'ai trouve les produits suivants :
- Beige Trench Coat | categorie: coat | couleur: beige | taille: M | prix: 149.99 EUR | stock: 7
- Beige Trench Coat | categorie: coat | couleur: beige | taille: L | prix: 149.99 EUR | stock: 4 | category synonym risk | OK |

## Failure Categories To Track

- routing error
- support answer quality issue
- product parsing issue
- follow-up memory issue
- catalog coverage limitation
